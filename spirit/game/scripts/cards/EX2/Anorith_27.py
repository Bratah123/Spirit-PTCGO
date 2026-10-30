from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.session.effects import is_evolution_pokemon


card = PokemonCardDef(
    guid="96351595-883f-541f-863d-8fcef9365739",
    key="EX2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Anorith.Name",
    display_name="Anorith",
    searchable_by=["Anorith", "Stage 1", "Anorith"],
    subtypes=["Stage 1"],
    collector_number=27,
    set_code="EX2",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.ClawFossil.Name",
    family_id=347,
    abilities=[
        Attack(
            title="Fast Evolution",
            game_text="Search your deck for an Evolution card, show it to your opponent, and put it into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_to_hand(
                is_evolution_pokemon,
                prompt="Choose an Evolution card to put into your hand.",
            ),
        ),
        Attack(
            title="Pierce",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)
