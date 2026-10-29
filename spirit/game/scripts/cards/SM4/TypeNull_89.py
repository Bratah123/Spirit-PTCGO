from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import protect_next_turn


card = PokemonCardDef(
    guid="bf599da2-4ca8-5ccc-8232-698bba431d64",
    key="SM4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TypeNull.Name",
    display_name="Type: Null",
    searchable_by=["Type: Null", "Basic", "TypeNull"],
    subtypes=["Basic"],
    collector_number=89,
    set_code="SM4",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=772,
    abilities=[
        Attack(
            title="Armor Press",
            game_text="During your opponent's next turn, this Pok\u00e9mon takes 30 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            # STUB: attack effect not implemented
            effect=protect_next_turn(reduce=30),
        ),
        Attack(
            title="Slashing Claw",
            cost={PokemonTypes.COLORLESS: 3},
            damage=70,
        ),
    ],
)