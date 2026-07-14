from spirit.game.card_effects.attacks_common import count_energy, damage_per
from spirit.game.card_effects.support_common import switch_self_attack
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="31a2aa43-d566-5931-88ef-60930a7b69b2",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.OrbeetleV.Name",
    display_name="Orbeetle V",
    searchable_by=["Orbeetle V", "Basic", "V", "OrbeetleV"],
    subtypes=["Basic", "V"],
    collector_number=20,
    set_code="SWSH4",
    rarity=Rarities.RareHoloV,
    hp=180,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=826,
    abilities=[
        Attack(
            title="Strafe",
            game_text="You may switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
            effect=switch_self_attack(optional=True),
        ),
        Attack(
            title="Mysterious Wave",
            game_text="This attack does 30 more damage for each Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator="+",
            effect=damage_per(count_energy("defender"), 30, base=50),
        ),
    ],
)