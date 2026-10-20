from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import gust_attack
from spirit.game.card_effects.attacks_common import recoil_attack

card = PokemonCardDef(
    guid="1db0b812-6672-5142-8664-094969c7c271",
    key="BW2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sawsbuck.Name",
    display_name="Sawsbuck",
    searchable_by=["Sawsbuck", "Stage 1", "Sawsbuck"],
    subtypes=["Stage 1"],
    collector_number=16,
    set_code="BW2",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Deerling.Name",
    family_id=585,
    abilities=[
        Attack(
            title="Push Down",
            game_text="Your opponent switches the Defending Pok\u00e9mon with 1 of his or her Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=gust_attack(opponent_chooses=True),
        ),
        Attack(
            title="Take Down",
            game_text="This Pok\u00e9mon does 20 damage to itself.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=recoil_attack(20),
        ),
    ],
)