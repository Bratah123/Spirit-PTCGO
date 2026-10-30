from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import recoil_attack


card = PokemonCardDef(
    guid="d54c95c0-f6e8-5f33-a49f-c8188d3e81d1",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ErikasBellsprout.Name",
    display_name="Erika's Bellsprout",
    searchable_by=["Erika's Bellsprout", "Basic", "ErikasBellsprout"],
    subtypes=["Basic"],
    collector_number=76,
    set_code="GYM1",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=69,
    abilities=[
        Attack(
            title="Careless Tackle",
            game_text="Erika's Bellsprout does 10 damage to itself.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=recoil_attack(10),
        ),
    ],
)
