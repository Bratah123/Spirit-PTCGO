from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import heal_targets

card = PokemonCardDef(
    guid="b9d03e4e-e028-5a99-9ffc-7a9f7a83fdb1",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cutiefly.Name",
    display_name="Cutiefly",
    searchable_by=["Cutiefly", "Basic", "Cutiefly"],
    subtypes=["Basic"],
    collector_number=145,
    set_code="SM8",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=742,
    abilities=[
        Attack(
            title="Sweet Scent",
            game_text="Heal 30 damage from 1 of your Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=heal_targets(30, 'choice'),
        ),
    ],
)