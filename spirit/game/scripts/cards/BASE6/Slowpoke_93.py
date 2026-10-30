from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import (
    has_typed_basic_energy, scavenge, self_is_damaged, spacing_out,
)


card = PokemonCardDef(
    guid="3566b3d2-d2cb-5f83-ad15-d4c5f3866b28",
    key="BASE6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Slowpoke.Name",
    display_name="Slowpoke",
    searchable_by=["Slowpoke", "Basic", "Slowpoke"],
    subtypes=["Basic"],
    collector_number=93,
    set_code="BASE6",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=79,
    abilities=[
        Attack(
            title="Spacing Out",
            game_text="Flip a coin. If heads, remove a damage counter from Slowpoke. This attack can't be used if Slowpoke has no damage counters on it.",
            cost={PokemonTypes.COLORLESS: 1},
            condition=self_is_damaged,
            effect=spacing_out,
        ),
        Attack(
            title="Scavenge",
            game_text="Discard 1 Psychic Energy card attached to Slowpoke in order to use this attack. Put a Trainer card from your discard pile into your hand.",
            cost={PokemonTypes.PSYCHIC: 2},
            condition=has_typed_basic_energy(PokemonTypes.PSYCHIC),
            effect=scavenge,
        ),
    ],
)
