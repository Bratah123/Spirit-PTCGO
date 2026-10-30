"""DP4 Great Encounters — wired.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import amnesia


card = PokemonCardDef(
    guid="717819cc-6fc0-5104-bdd4-262c0f3a167a",
    key="DP4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Slowbro.Name",
    display_name="Slowbro",
    searchable_by=["Slowbro", "Stage 1", "Slowbro"],
    subtypes=["Stage 1"],
    collector_number=54,
    set_code="DP4",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Slowpoke.Name",
    family_id=79,
    abilities=[
        Attack(
            title="Amnesia",
            game_text="Choose 1 of the Defending Pok\u00e9mon's attacks. That Pok\u00e9mon can't use that attack during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            # STUB: attack effect not implemented
            effect=amnesia,
        ),
        Attack(
            title="Zen Headbutt",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
    ],
)