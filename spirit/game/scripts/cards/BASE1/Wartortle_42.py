from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import flip_protection


card = PokemonCardDef(
    guid="7b66bdc1-8164-5a19-b83d-2a3263ace97f",
    key="BASE1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wartortle.Name",
    display_name="Wartortle",
    searchable_by=["Wartortle", "Stage 1", "Wartortle"],
    subtypes=["Stage 1"],
    collector_number=42,
    set_code="BASE1",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Squirtle.Name",
    family_id=7,
    abilities=[
        Attack(
            title="Withdraw",
            game_text="Flip a coin. If heads, prevent all damage done to Wartortle during your opponent's next turn. (Any other effects of attacks still happen.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            effect=flip_protection(prevent=True),
        ),
        Attack(
            title="Bite",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
    ],
)
