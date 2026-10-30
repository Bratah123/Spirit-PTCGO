from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import heal_equal_to_damage

card = PokemonCardDef(
    guid="a4d03138-ed9c-50da-b09c-1ae6339c3ae6",
    key="EX3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Nincada.Name",
    display_name="Nincada",
    searchable_by=["Nincada", "Basic", "Nincada"],
    subtypes=["Basic"],
    collector_number=68,
    set_code="EX3",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=290,
    abilities=[
        Attack(
            title="Leech Life",
            game_text="After your attack, remove from Nincada the number of damage counters equal to the damage you did to the Defending Pok\u00e9mon. If Nincada has fewer damage counters than that, remove all of them.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=heal_equal_to_damage(),
        ),
    ],
)