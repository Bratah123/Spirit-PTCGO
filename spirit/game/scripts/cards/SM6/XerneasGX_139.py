from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import snipe_attack
from spirit.game.card_effects.sm6 import sanctuary_gx

card = PokemonCardDef(
    guid="82956052-b9c2-5bcc-a518-61f1ff3449c2",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.XerneasGX.Name",
    display_name="Xerneas-GX",
    searchable_by=["Xerneas-GX", "Basic", "GX", "XerneasGX"],
    subtypes=["Basic", "GX"],
    collector_number=139,
    set_code="SM6",
    rarity=Rarities.RareRainbow,
    hp=180,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=716,
    abilities=[
        Attack(
            title="Overrun",
            game_text="This attack does 20 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=snipe_attack(20, also_base=True),
        ),
        Attack(
            title="Aurora Horns",
            cost={PokemonTypes.FAIRY: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
        ),
        Attack(
            title="Sanctuary-GX",
            game_text="Move all damage counters from each of your Pok\u00e9mon to your opponent's Active Pok\u00e9mon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.FAIRY: 2, PokemonTypes.COLORLESS: 1},
            effect=sanctuary_gx,
        ),
    ],
)
