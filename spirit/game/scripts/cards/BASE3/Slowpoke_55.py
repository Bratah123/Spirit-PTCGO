from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import (
    has_typed_basic_energy, scavenge, self_is_damaged, spacing_out,
)


card = PokemonCardDef(
    guid="2ed3486f-46bb-5f11-a1b4-d319b8e07550",
    key="BASE3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Slowpoke.Name",
    display_name="Slowpoke",
    searchable_by=["Slowpoke", "Basic", "Slowpoke"],
    subtypes=["Basic"],
    collector_number=55,
    set_code="BASE3",
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
