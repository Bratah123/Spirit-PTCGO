from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import heal_targets


card = PokemonCardDef(
    guid="3a6fe586-2a2c-5788-8a49-e487551e6c7e",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Petilil.Name",
    display_name="Petilil",
    searchable_by=["Petilil", "Basic", "Petilil"],
    subtypes=["Basic"],
    collector_number=7,
    set_code="XY9",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=548,
    abilities=[
        Attack(
            title="Aromatherapy",
            game_text="Heal 10 damage from each of your Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1},
            effect=heal_targets(10, 'each_own'),
        ),
    ],
)