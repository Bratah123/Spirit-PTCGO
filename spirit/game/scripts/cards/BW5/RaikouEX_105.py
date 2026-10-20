from spirit.game.data_utils import PokemonCardDef, Attack, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="59ece66d-61cf-5d12-80c6-6573d2ad2485",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RaikouEX.Name",
    display_name="Raikou-EX",
    searchable_by=["Raikou-EX", "Basic", "EX", "RaikouEX"],
    subtypes=["Basic", "EX"],
    collector_number=105,
    set_code="BW5",
    rarity=Rarities.RareUltra,
    hp=170,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=243,
    abilities=[
        Attack(
            title="Thunder Fang",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
        Attack(
            title="Volt Bolt",
            game_text="Discard all Lightning Energy attached to this Pok\u00e9mon. This attack does 100 damage to 1 of your opponent's Pok\u00e9mon. (Don't apply Weakness or Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
    ],
)