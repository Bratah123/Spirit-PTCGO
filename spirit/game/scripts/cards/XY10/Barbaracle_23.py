from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.session.effects import is_special_energy


class _HandBlock(Passive):
    """If you have a Stadium in play, your opponent can't attach Special Energy from hand."""
    def blocks_energy_attach(self, energy, player_id, target, carrier):
        me = carrier_pokemon(carrier)
        if me is None or player_id == me.owning_player_id or not is_special_energy(energy):
            return False
        node = getattr(me, "parent", None)
        while node is not None and getattr(node, "parent", None) is not None:
            node = node.parent
        stadium = _find_stadium(node)
        return stadium is not None and stadium.owning_player_id == me.owning_player_id


def _find_stadium(root):
    stack = [root] if root is not None else []
    while stack:
        n = stack.pop()
        try:
            if n.get_attribute(AttrID.NAME) == "activeStadium":
                return n.children[0] if n.children else None
        except Exception:
            pass
        stack.extend(getattr(n, "children", []) or [])
    return None


card = PokemonCardDef(
    guid="59beef1e-32dc-5044-b7ba-f18cb5d2b858",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Barbaracle.Name",
    display_name="Barbaracle",
    searchable_by=["Barbaracle", "Stage 1", "Barbaracle"],
    subtypes=["Stage 1"],
    collector_number=23,
    set_code="XY10",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Binacle.Name",
    family_id=688,
    abilities=[
        Ability(
            title="Hand Block",
            game_text="If you have a Stadium card in play, your opponent can't attach any Special Energy cards from his or her hand to his or her Pok\u00e9mon.",
            passive=_HandBlock(),
        ),
        Attack(
            title="Claw Slash",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
        ),
    ],
)