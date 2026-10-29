from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.card_effects.support_common import search_attach_energy
from spirit.game.card_effects.smp import luster_purge


card = PokemonCardDef(
    guid="18cf9f10-3edf-513c-89aa-d20d8603df15",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Latios.Name",
    display_name="Latios",
    searchable_by=["Latios", "Basic", "Latios"],
    subtypes=["Basic"],
    collector_number=136,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=120,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FAIRY,
    family_id=381,
    abilities=[
        Attack(
            title="Energy Extract",
            game_text="Search your deck for a basic Energy card and attach it to this Pok\u00e9mon. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=search_attach_energy(predicate=is_basic_energy_card, count=1, to_self=True),
        ),
        Attack(
            title="Luster Purge",
            game_text="Flip a coin. If tails, discard all Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=140,
            effect=luster_purge,
        ),
    ],
)