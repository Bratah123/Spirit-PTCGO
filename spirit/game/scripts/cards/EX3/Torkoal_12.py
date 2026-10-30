from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import recover_from_discard
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.card_effects.ex import burn_flip_tails_discard_energy

card = PokemonCardDef(
    guid="862f6fae-e2c2-5f06-955e-fa1b1a9e0dcc",
    key="EX3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Torkoal.Name",
    display_name="Torkoal",
    searchable_by=["Torkoal", "Basic", "Torkoal"],
    subtypes=["Basic"],
    collector_number=12,
    set_code="EX3",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    family_id=324,
    abilities=[
        Attack(
            title="Power Generation",
            game_text="Search your discard pile for up to 2 basic Energy cards, show them to your opponent, and put them into your hand.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=recover_from_discard(predicate=is_basic_energy_card, count=2, minimum=0, reveal=True),
        ),
        Attack(
            title="Scorching Smoke",
            game_text="The Defending Pok\u00e9mon is now Burned. Flip a coin. If tails, discard a Fire Energy card attached to Torkoal.",
            cost={PokemonTypes.FIRE: 1},
            # STUB: attack effect not implemented
            effect=burn_flip_tails_discard_energy(PokemonTypes.FIRE),
        ),
    ],
)