from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if, damage_counters_on
from spirit.game.card_effects.support_common import heal_attack

card = PokemonCardDef(
    guid="88bf3243-6420-5365-9449-6de59cd6dbbf",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Copperajah.Name",
    display_name="Copperajah",
    searchable_by=["Copperajah", "Stage 1", "Copperajah"],
    subtypes=["Stage 1"],
    collector_number=137,
    set_code="SWSH1",
    rarity=Rarities.RareHolo,
    hp=190,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cufant.Name",
    family_id=878,
    abilities=[
        Attack(
            title="Dig Drain",
            game_text="Heal 30 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.METAL: 2},
            damage=60,
            effect=heal_attack(30),
        ),
        Attack(
            title="Muscular Nose",
            game_text="If this Pok\u00e9mon has 8 or more damage counters on it, this attack does nothing.",
            cost={PokemonTypes.METAL: 3},
            damage=220,
            effect=bonus_if(
                lambda ctx: damage_counters_on("self")(ctx) < 8, 0, else_nothing=True
            ),
        ),
    ],
)