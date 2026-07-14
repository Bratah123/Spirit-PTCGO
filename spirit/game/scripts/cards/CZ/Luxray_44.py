from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.session.effects import is_trainer_card

card = PokemonCardDef(
    guid="ef8ca3ef-7c49-55f9-8a3b-0bf871f8e524",
    key="CZ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Luxray.Name",
    display_name="Luxray",
    searchable_by=["Luxray", "Stage 2", "Luxray"],
    subtypes=["Stage 2"],
    collector_number=44,
    set_code="CZ",
    rarity=Rarities.Rare,
    hp=160,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Luxio.Name",
    family_id=403,
    setup_as_active=True,
    abilities=[
        Ability(
            title="Explosiveness",
            game_text="If this Pok\u00e9mon is in your hand when you are setting up to play, you may put it face down as your Active Pok\u00e9mon.",
        ),
        Attack(
            title="Seeking Fang",
            game_text="Search your deck for up to 2 Trainer cards, reveal them, and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=search_to_hand(
                is_trainer_card, count=2, minimum=0,
                prompt="Choose up to 2 Trainer cards to put into your hand.",
            ),
        ),
    ],
)