from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import zzzap


card = PokemonCardDef(
    guid="dfd6bca4-26a3-5a22-8942-b7a0181dd6bb",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pichu.Name",
    display_name="Pichu",
    searchable_by=["Pichu", "Baby", "Pichu"],
    subtypes=["Baby"],
    collector_number=12,
    set_code="NEO1",
    rarity=Rarities.RareHolo,
    hp=30,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    family_id=172,
    abilities=[
        Attack(
            title="Zzzap",
            game_text="Does 20 damage to each Pok\u00e9mon in play that has a Pok\u00e9mon Power. Don't apply Weakness and Resistance.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=zzzap,
        ),
    ],
)
