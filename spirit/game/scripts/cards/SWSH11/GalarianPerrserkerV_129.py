from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import draw_attack
from spirit.game.card_effects.attacks_common import damage_per, count_hand

card = PokemonCardDef(
    guid="9e12d520-10c7-5a2e-b1be-ae6e0e5882ba",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianPerrserkerV.Name",
    display_name="Galarian Perrserker V",
    searchable_by=["Galarian Perrserker V", "Basic", "V", "GalarianPerrserkerV"],
    subtypes=["Basic", "V"],
    collector_number=129,
    set_code="SWSH11",
    rarity=Rarities.RareHoloV,
    hp=200,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=863,
    abilities=[
        Attack(
            title="Feelin' Fine",
            game_text="Draw 3 cards.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=draw_attack(3),
        ),
        Attack(
            title="Treasure Rush",
            game_text="This attack does 20 damage for each card in your hand.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="x",
            effect=damage_per(count_hand("mine"), 20),
        ),
    ],
)