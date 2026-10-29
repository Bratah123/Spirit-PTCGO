from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import AttrID
from spirit.game.card_effects.attacks_common import damage_per


def _defender_retreat_cost(ctx):
    defender = ctx.defender
    return int(defender.get_attribute(AttrID.RETREAT_COST) or 0) if defender else 0


card = PokemonCardDef(
    guid="b00946fa-308f-5c71-8f17-337ebd9be754",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wobbuffet.Name",
    display_name="Wobbuffet",
    searchable_by=["Wobbuffet", "Basic", "Wobbuffet"],
    subtypes=["Basic"],
    collector_number=49,
    set_code="SM3",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=202,
    abilities=[
        Attack(
            title="Shadowy Knot",
            game_text="This attack does 50 damage for each Colorless in your opponent's Active Pok\u00e9mon's Retreat Cost.",
            cost={PokemonTypes.PSYCHIC: 3},
            damage=50,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=damage_per(_defender_retreat_cost, 50),
        ),
    ],
)
