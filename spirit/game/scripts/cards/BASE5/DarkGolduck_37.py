from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import has_attached_energy, third_eye


card = PokemonCardDef(
    guid="46764d09-7b8a-5d48-a920-17d2695fdb80",
    key="BASE5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkGolduck.Name",
    display_name="Dark Golduck",
    searchable_by=["Dark Golduck", "Stage 1", "DarkGolduck"],
    subtypes=["Stage 1"],
    collector_number=37,
    set_code="BASE5",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Psyduck.Name",
    family_id=54,
    abilities=[
        Attack(
            title="Third Eye",
            game_text="Discard 1 Energy card attached to Dark Golduck in order to draw up to 3 cards.",
            cost={PokemonTypes.PSYCHIC: 1},
            condition=has_attached_energy,
            effect=third_eye,
        ),
        Attack(
            title="Super Psy",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)
