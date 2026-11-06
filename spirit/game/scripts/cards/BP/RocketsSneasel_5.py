from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import condition_attack, flip_damage


card = PokemonCardDef(
    guid="521cd0bd-b745-566c-b616-fcbb2404301e",
    key="BP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RocketsSneasel.Name",
    display_name="Rocket's Sneasel",
    searchable_by=["Rocket's Sneasel", "Basic", "RocketsSneasel"],
    subtypes=["Basic"],
    collector_number=5,
    set_code="BP",
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=215,
    abilities=[
        Attack(
            title="Entrap",
            game_text="The Defending Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=condition_attack(no_retreat=True),
        ),
        Attack(
            title="Continuous Scratch",
            game_text="Flip 4 coins. This attack does 10 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="x",
            effect=flip_damage(coins=4, per_heads=10),
        ),
    ],
)
