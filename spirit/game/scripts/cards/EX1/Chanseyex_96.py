from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import recoil_attack
from spirit.game.card_effects.ex import heal_each_except_user


card = PokemonCardDef(
    guid="2b304fea-68c3-5572-be63-9ae9068a5e22",
    key="EX1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Chanseyex.Name",
    display_name="Chansey ex",
    searchable_by=["Chansey ex", "Basic", "ex", "Chanseyex"],
    subtypes=["Basic", "ex"],
    collector_number=96,
    set_code="EX1",
    rarity=Rarities.RareHoloEX,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=113,
    abilities=[
        Attack(
            title="Healing Egg",
            game_text="Remove 2 damage counters (1 if there is only 1) from each of your Pok\u00e9mon. Remove no damage counters from Chansey ex.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=heal_each_except_user(20),
        ),
        Attack(
            title="Double-edge",
            game_text="Chansey ex does 60 damage to itself.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
            effect=recoil_attack(60),
        ),
    ],
)
