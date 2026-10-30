"""Technical Machine TS-1 (DP6 #136)."""
from spirit.game.data_utils import PokemonToolCardDef, Attack
from spirit.game.attributes import Rarities, PokemonTypes
from spirit.game.card_effects.dp import tm_ts1_evoluter, tm_grants_attack_passive

def _evoluter():
    return Attack(
        title="Evoluter",
        game_text="Search your deck for a card that evolves from 1 of your Pokémon and put it onto that Pokémon. (This counts as evolving that Pokémon.) Shuffle your deck afterward.",
        cost={},
        effect=tm_ts1_evoluter(),
    )

card = PokemonToolCardDef(
    guid="65de453d-0f58-56c9-8c0e-1c3996e89f3f",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TechnicalMachineTS1.Name",
    display_name="Technical Machine TS-1",
    searchable_by=["Technical Machine TS-1", "Technical Machine"],
    subtypes=["Technical Machine"],
    collector_number=136,
    set_code="DP6",
    rarity=Rarities.Uncommon,
    passive=tm_grants_attack_passive(_evoluter),
)
