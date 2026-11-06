from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import recoil_attack
from spirit.game.card_effects.support_common import gust_attack


card = PokemonCardDef(
    guid="63473ee2-1834-5232-926a-bd946b5d514d",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BrocksRhyhorn.Name",
    display_name="Brock's Rhyhorn",
    searchable_by=["Brock's Rhyhorn", "Basic", "BrocksRhyhorn"],
    subtypes=["Basic"],
    collector_number=22,
    set_code="GYM1",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    resistance_type=PokemonTypes.LIGHTNING,
    family_id=111,
    abilities=[
        Attack(
            title="Horn Toss",
            game_text="If your opponent has any Benched Pok\u00e9mon, he or she chooses 1 of them and switches it with the Defending Pok\u00e9mon. (Do the damage before switching the Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=gust_attack(opponent_chooses=True),
        ),
        Attack(
            title="Take Down",
            game_text="Brock's Rhyhorn does 10 damage to itself.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=recoil_attack(10),
        ),
    ],
)
