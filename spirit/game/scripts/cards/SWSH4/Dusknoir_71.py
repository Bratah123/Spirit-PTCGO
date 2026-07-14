from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.passives import Passive


class SpectralBreachPassive(Passive):
    """All Special Energy (both players') provide only Colorless Energy."""

    def suppresses_special_energy(self, energy, carrier) -> bool:
        return True


card = PokemonCardDef(
    guid="2547c701-72a5-5fd2-9cee-3552a1f4da1c",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dusknoir.Name",
    display_name="Dusknoir",
    searchable_by=["Dusknoir", "Stage 2", "Dusknoir"],
    subtypes=["Stage 2"],
    collector_number=71,
    set_code="SWSH4",
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dusclops.Name",
    family_id=355,
    abilities=[
        Ability(
            title="Spectral Breach",
            game_text="All Special Energy attached to Pokémon (both yours and your opponent's) provide Colorless Energy and have no other effect.",
            passive=SpectralBreachPassive(),
        ),
        Attack(
            title="Spooky Shot",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
        ),
    ],
)
