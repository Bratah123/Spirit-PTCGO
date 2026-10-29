from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.sm4 import SurgeSurferPassive, psychic_70_plus

card = PokemonCardDef(
    guid="74e1deec-4fcc-5b78-8eee-005592c591a2",
    key="SM4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanRaichu.Name",
    display_name="Alolan Raichu",
    searchable_by=["Alolan Raichu", "Stage 1", "AlolanRaichu"],
    subtypes=["Stage 1"],
    collector_number=31,
    set_code="SM4",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pikachu.Name",
    family_id=25,
    abilities=[
        Ability(
            title="Surge Surfer",
            game_text="If there is any Stadium card in play, this Pok\u00e9mon has no Retreat Cost.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=SurgeSurferPassive(),
        ),
        Attack(
            title="Psychic",
            game_text="This attack does 20 more damage times the amount of Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=70,
            damage_operator="+",
            effect=psychic_70_plus,
        ),
    ],
)