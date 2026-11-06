from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import (
    has_typed_basic_energy, recover_discarding_energy,
)


card = PokemonCardDef(
    guid="b2419304-d554-521b-ab9c-2cff1078e8e4",
    key="BASE4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kadabra.Name",
    display_name="Kadabra",
    searchable_by=["Kadabra", "Stage 1", "Kadabra"],
    subtypes=["Stage 1"],
    collector_number=46,
    set_code="BASE4",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Abra.Name",
    family_id=63,
    abilities=[
        Attack(
            title="Recover",
            game_text="Discard 1 Psychic Energy card attached to Kadabra in order to use this attack. Remove all damage counters from Kadabra.",
            cost={PokemonTypes.PSYCHIC: 2},
            condition=has_typed_basic_energy(PokemonTypes.PSYCHIC),
            effect=recover_discarding_energy(PokemonTypes.PSYCHIC),
        ),
        Attack(
            title="Super Psy",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)
