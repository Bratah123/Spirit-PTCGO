from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import lightning_storm, zzzap


card = PokemonCardDef(
    guid="f5e02f3e-1534-56b2-b7d9-f749535a0083",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Raichu.Name",
    display_name="Raichu",
    searchable_by=["Raichu", "Stage 1", "Raichu"],
    subtypes=["Stage 1"],
    collector_number=27,
    set_code="ECARD3",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pikachu.Name",
    family_id=25,
    abilities=[
        Attack(
            title="Zzzap",
            game_text="This attack does 20 damage to each Pok\u00e9mon with a Pok\u00e9-Body or Pok\u00e9-Power (yours and your opponent's). (Don't apply Weakness or Resistance.)",
            cost={PokemonTypes.COLORLESS: 2},
            effect=zzzap,
        ),
        Attack(
            title="Lightning Storm",
            game_text="Flip a coin. If tails, put 2 damage counters on Raichu.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=lightning_storm,
        ),
    ],
)
