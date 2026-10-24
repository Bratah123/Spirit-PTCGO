from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack, place_counters


card = PokemonCardDef(
    guid="45732293-ce7a-535d-8272-718247a77104",
    key="BW11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ChandelureEX.Name",
    display_name="Chandelure-EX",
    searchable_by=["Chandelure-EX", "Basic", "EX", "ChandelureEX"],
    subtypes=["Basic", "EX"],
    collector_number=77,
    set_code="BW11",
    rarity=Rarities.RareHoloEX,
    hp=170,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    family_id=609,
    abilities=[
        Attack(
            title="Cursed Drop",
            game_text="Put 4 damage counters on your opponent's Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=place_counters(4, 'choose_any_opponent'),
        ),
        Attack(
            title="Eerie Glow",
            game_text="The Defending Pok\u00e9mon is now Burned and Confused.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
            effect=condition_attack(SpecialConditions.BURNED, SpecialConditions.CONFUSED),
        ),
    ],
)