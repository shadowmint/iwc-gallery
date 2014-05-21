(() => {
    var owner = document['_currentScript'].ownerDocument;
    var tmpl = owner.getElementById('hello_gallery');
    var prototype = Object.create(HTMLElement.prototype);
    prototype.createdCallback = function () {
        var root = this.createShadowRoot();
        var clone = document.importNode(tmpl['content'], true);
        root.appendChild(clone);
    };
    document['registerElement']('hello-gallery', {
        prototype: prototype
    });
})();

