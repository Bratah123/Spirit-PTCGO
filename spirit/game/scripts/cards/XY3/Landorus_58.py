from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import attach_from_discard
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.card_effects.passives_common import is_in_active_spot


card = PokemonCardDef(
    guid="1124aa45-bd86-5ef5-84d9-7f9ada3d3633",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Landorus.Name",
    display_name="Landorus",
    searchable_by=["Landorus", "Basic", "Landorus"],
    subtypes=["Basic"],
    collector_number=58,
    set_code="XY3",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=645,
    abilities=[
        Attack(
            title="Shout of Power",
            game_text="Attach a basic Energy card from your discard pile to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
            effect=attach_from_discard(predicate=is_basic_energy_card, count=1, target=lambda p: not is_in_active_spot(p), prompt='Choose a basic Energy card to attach to a Benched Pokémon'),
        ),
        Attack(
            title="Sky Lariat",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
        ),
    ],
)