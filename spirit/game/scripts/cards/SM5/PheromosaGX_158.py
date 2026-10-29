from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.sm5 import beauty_gx

card = PokemonCardDef(
    guid="25858464-1f53-5807-90a3-16380820a150",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PheromosaGX.Name",
    display_name="Pheromosa-GX",
    searchable_by=["Pheromosa-GX", "Basic", "GX", "Ultra Beast", "PheromosaGX"],
    subtypes=["Basic", "GX", "Ultra Beast"],
    collector_number=158,
    set_code="SM5",
    rarity=Rarities.RareRainbow,
    hp=170,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=795,
    abilities=[
        Attack(
            title="Fast Raid",
            game_text="If you go first, you can use this attack on your first turn.",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            usable_first_turn=True,
        ),
        Attack(
            title="Cruel Spike",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.GRASS: 2},
            damage=60,
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.CONFUSED),
        ),
        Attack(
            title="Beauty-GX",
            game_text="This attack does 50 damage for each Prize card your opponent has taken. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.GRASS: 2},
            damage=50,
            damage_operator="x",
            effect=beauty_gx,
        ),
    ],
)