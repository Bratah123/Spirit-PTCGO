from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import heal_attack


card = PokemonCardDef(
    guid="7c1c2171-084f-5ab7-8649-e0b84a909119",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ralts.Name",
    display_name="Ralts",
    searchable_by=["Ralts", "Basic", "Ralts"],
    subtypes=["Basic"],
    collector_number=91,
    set_code="SM3",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=280,
    abilities=[
        Attack(
            title="Draining Kiss",
            game_text="Heal 10 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.FAIRY: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=heal_attack(10),
        ),
    ],
)
