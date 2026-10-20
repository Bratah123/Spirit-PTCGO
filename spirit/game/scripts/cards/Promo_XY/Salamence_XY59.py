from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import mill_attack
from spirit.game.card_effects.support_common import search_to_bench


card = PokemonCardDef(
    guid="9582869f-7c4b-5c94-9a06-aba5afdd7cdb",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Salamence.Name",
    display_name="Salamence",
    searchable_by=["Salamence", "Stage 2", "Salamence"],
    subtypes=["Stage 2"],
    collector_number=59,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=150,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FAIRY,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Shelgon.Name",
    family_id=373,
    abilities=[
        Attack(
            title="Call for Goons",
            game_text="Search your deck for up to 3 Basic Pok\u00e9mon and put them onto your Bench. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_to_bench(count=3),
        ),
        Attack(
            title="Dragon Pulse",
            game_text="Discard the top card of your deck.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=130,
            effect=mill_attack(1, opponent=False),
        ),
    ],
)