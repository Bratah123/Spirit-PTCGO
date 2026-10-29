from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.smp import time_recall_passive

card = PokemonCardDef(
    guid="8e353f1b-7773-5e66-9e46-62c8f2c6c6df",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ShiningCelebi.Name",
    display_name="Shining Celebi",
    searchable_by=["Shining Celebi", "Basic", "ShiningCelebi"],
    subtypes=["Basic"],
    collector_number=79,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=251,
    abilities=[
        Ability(
            title="Time Recall",
            game_text="Each of your evolved Pok\u00e9mon can use any attack from its previous Evolutions. (You still need the necessary Energy to use each attack.)",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=time_recall_passive,
        ),
        Attack(
            title="Leaf Step",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)