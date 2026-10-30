from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import thunder_jolt_self

card = PokemonCardDef(
    guid="bff7a879-b5c5-50c0-aa35-42058450c445",
    key="POP5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Charmeleon.Name",
    display_name="Charmeleon δ",
    searchable_by=["Charmeleon \u03b4", "Stage 1", "Charmeleon"],
    subtypes=["Stage 1"],
    collector_number=5,
    set_code="POP5",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Charmander.Name",
    family_id=4,
    abilities=[
        Attack(
            title="Slash",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
        Attack(
            title="Thunder Jolt",
            game_text="Flip a coin. If tails, Charmeleon does 10 damage to itself.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
                        effect=thunder_jolt_self(10),
        ),
    ],
)