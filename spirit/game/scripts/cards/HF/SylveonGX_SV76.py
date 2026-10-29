from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.scripts.cards.SM2.SylveonGX_92 import plea_gx
from spirit.game.card_effects.support_common import search_to_hand

card = PokemonCardDef(
    guid="603c08e0-c22f-56eb-9015-09c48d51a19e",
    key="HF",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SylveonGX.Name",
    display_name="Sylveon-GX",
    searchable_by=["Sylveon-GX", "Stage 1", "GX", "SylveonGX"],
    subtypes=["Stage 1", "GX"],
    collector_number=145,
    set_code="HF",
    rarity=Rarities.RareUltra,
    hp=200,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=700,
    abilities=[
        Attack(
            title="Magical Ribbon",
            game_text="Search your deck for up to 3 cards and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.FAIRY: 1},
            effect=search_to_hand(None, count=3, minimum=0, reveal=False, prompt='Choose up to 3 cards'),
        ),
        Attack(
            title="Fairy Wind",
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 2},
            damage=110,
        ),
        Attack(
            title="Plea-GX",
            game_text="Put 2 of your opponent's Benched Pok\u00e9mon and all cards attached to them into your opponent's hand. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 2},
            effect=plea_gx,
        ),
    ],
)