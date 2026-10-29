from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="d46b99f2-327b-5da1-a814-5e99264e0123",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Stufful.Name",
    display_name="Stufful",
    searchable_by=["Stufful", "Basic", "Stufful"],
    subtypes=["Basic"],
    collector_number=110,
    set_code="SM3",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=759,
    abilities=[
        Attack(
            title="Baby-Doll Eyes",
            game_text="The Defending Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=condition_attack(no_retreat=True),
        ),
        Attack(
            title="Tackle",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
