from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import recoil_attack
from spirit.game.card_effects.support_common import gust_attack


card = PokemonCardDef(
    guid="af4b5285-23d5-5020-a706-871de63db032",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BlainesGrowlithe.Name",
    display_name="Blaine's Growlithe",
    searchable_by=["Blaine's Growlithe", "Basic", "BlainesGrowlithe"],
    subtypes=["Basic"],
    collector_number=35,
    set_code="GYM1",
    rarity=Rarities.Uncommon,
    hp=50,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=58,
    abilities=[
        Attack(
            title="Shake",
            game_text="If your opponent has any Benched Pok\u00e9mon, he or she chooses 1 of them and switches it with the Defending Pok\u00e9mon. (Do the damage before switching the Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=gust_attack(opponent_chooses=True),
        ),
        Attack(
            title="Fire Tackle",
            game_text="Blaine's Growlithe does 10 damage to itself.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=recoil_attack(10),
        ),
    ],
)
