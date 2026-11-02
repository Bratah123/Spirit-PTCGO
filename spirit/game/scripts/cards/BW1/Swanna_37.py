from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import apply_own_next_turn_boost
from spirit.game.card_effects.support_common import switch_self_attack


async def feather_dance(ctx):
    """During your next turn, this Pokémon's attacks do +40."""
    await apply_own_next_turn_boost(ctx, 40)


card = PokemonCardDef(
    guid="f9452323-9b0d-5d74-8066-f31b27aa1d1a",
    key="BW1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Swanna.Name",
    display_name="Swanna",
    searchable_by=["Swanna", "Stage 1", "Swanna"],
    subtypes=["Stage 1"],
    collector_number=37,
    set_code="BW1",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Ducklett.Name",
    family_id=580,
    abilities=[
        Attack(
            title="Feather Dance",
            game_text="During your next turn, each of this Pok\u00e9mon's attacks does 40 more damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 1},
            effect=feather_dance,
        ),
        Attack(
            title="Aqua Ring",
            game_text="Switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=switch_self_attack(),
        ),
    ],
)
