from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import deflector


card = PokemonCardDef(
    guid="60dd2002-1bf9-5aca-840c-c2e6bdb028e6",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Chikorita.Name",
    display_name="Chikorita",
    searchable_by=["Chikorita", "Basic", "Chikorita"],
    subtypes=["Basic"],
    collector_number=53,
    set_code="NEO1",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=152,
    abilities=[
        Attack(
            title="Tackle",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Deflector",
            game_text="During your opponent's next turn, whenever Chikorita takes damage, divide that damage in half (rounded down to the nearest 10). (Any other effects still happen.)",
            cost={PokemonTypes.GRASS: 1},
            effect=deflector,
        ),
    ],
)
