from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import opponent_has_benched
from spirit.game.card_effects.support_common import gust_attack


card = PokemonCardDef(
    guid="ca4bf4af-10d4-5484-8847-3ceb33cc3769",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ErikasWeepinbell.Name",
    display_name="Erika's Weepinbell",
    searchable_by=["Erika's Weepinbell", "Stage 1", "ErikasWeepinbell"],
    subtypes=["Stage 1"],
    collector_number=48,
    set_code="GYM1",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.ErikasBellsprout.Name",
    family_id=69,
    abilities=[
        Attack(
            title="Drool",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
        ),
        Attack(
            title="Flytrap",
            game_text="Before doing damage, choose 1 of your opponent's Benched Pok\u00e9mon and switch it with his or her Active Pok\u00e9mon. This attack can't be used if your opponent has no Benched Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 2},
            damage=20,
            condition=opponent_has_benched,
            effect=gust_attack(damage_to_new_active=20, damage_before=0),
        ),
    ],
)
