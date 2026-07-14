from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import AttrID
from spirit.game.session.passives import Passive


class _FieldRunnerPassive(Passive):
    """No Retreat Cost while a Stadium is in play."""

    def modify_retreat_cost(self, cost, pokemon, carrier, board):
        if pokemon is not carrier:
            return cost
        node = carrier
        while node.parent is not None:
            node = node.parent
        for child in node.children:
            if child.get_attribute(AttrID.NAME) == "activeStadium" and child.children:
                return 0
        return cost


card = PokemonCardDef(
    guid="c33475c2-20c9-54c7-8ac8-7721bc54baac",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CinderaceV.Name",
    display_name="Cinderace V",
    searchable_by=["Cinderace V", "Basic", "V", "CinderaceV"],
    subtypes=["Basic", "V"],
    collector_number=35,
    set_code="SWSH2",
    rarity=Rarities.RareHoloV,
    hp=210,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=815,
    abilities=[
        Ability(
            title="Field Runner",
            game_text="If a Stadium is in play, this Pok\u00e9mon has no Retreat Cost.",
            passive=_FieldRunnerPassive(),
        ),
        Attack(
            title="Crimson Legs",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=140,
        ),
    ],
)