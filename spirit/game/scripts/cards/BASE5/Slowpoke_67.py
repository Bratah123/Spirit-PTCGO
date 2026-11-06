from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import search_attach_energy
from spirit.game.card_effects.trainers import is_psychic_energy_card


card = PokemonCardDef(
    guid="c5f3dccd-ee25-5306-a4e3-b755c74ded83",
    key="BASE5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Slowpoke.Name",
    display_name="Slowpoke",
    searchable_by=["Slowpoke", "Basic", "Slowpoke"],
    subtypes=["Basic"],
    collector_number=67,
    set_code="BASE5",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=79,
    abilities=[
        Attack(
            title="Afternoon Nap",
            game_text="Search your deck for a Psychic Energy card and attach it to Slowpoke. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_attach_energy(
                predicate=is_psychic_energy_card, count=1, to_self=True,
                prompt="Choose a Psychic Energy card to attach to Slowpoke.",
            ),
        ),
        Attack(
            title="Headbutt",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
        ),
    ],
)
