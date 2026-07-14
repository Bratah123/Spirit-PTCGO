from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.attacks_common import snipe_attack
from spirit.game.session.effects import is_item_card

card = PokemonCardDef(
    guid="57328661-1060-546e-aaef-111692e4f69a",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MagnezoneVSTAR.Name",
    display_name="Magnezone VSTAR",
    searchable_by=["Magnezone VSTAR", "VSTAR", "MagnezoneVSTAR"],
    subtypes=["VSTAR"],
    collector_number=57,
    set_code="SWSH11",
    rarity=Rarities.RareHoloVSTAR,
    hp=270,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.VSTAR,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.MagnezoneV.Name",
    family_id=462,
    abilities=[
        Attack(
            title="Magnetic Grip",
            game_text="Search your deck for up to 2 Item cards, reveal them, and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=180,
            effect=search_to_hand(is_item_card, count=2, minimum=0, reveal=True),
        ),
        Attack(
            title="Electro Star",
            game_text="This attack does 90 damage to 2 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.) (You can't use more than 1 VSTAR Power in a game.)",
            cost={PokemonTypes.LIGHTNING: 2},
            vstar=True,
            effect=snipe_attack(90, pool="bench", count=2),
        ),
    ],
)