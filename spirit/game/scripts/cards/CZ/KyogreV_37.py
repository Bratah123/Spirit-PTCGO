from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import snipe_attack

card = PokemonCardDef(
    guid="4403b192-7c0c-5597-a32d-56a4686d0b6b",
    key="CZ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.KyogreV.Name",
    display_name="Kyogre V",
    searchable_by=["Kyogre V", "Basic", "V", "KyogreV"],
    subtypes=["Basic", "V"],
    collector_number=37,
    set_code="CZ",
    rarity=Rarities.RareHoloV,
    hp=230,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=382,
    abilities=[
        Attack(
            title="Dual Splash",
            game_text="This attack does 50 damage to 2 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            effect=snipe_attack(50, pool="any", count=2, side="opponent"),
        ),
        Attack(
            title="Aqua Typhoon",
            game_text="During your next turn, this Pok\u00e9mon can't use Aqua Typhoon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 3},
            damage=210,
            locks_next_turn=True,
        ),
    ],
)