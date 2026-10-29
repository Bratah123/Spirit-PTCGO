from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.sm12 import lost_march

card = PokemonCardDef(
    guid="2714d458-34ad-538a-a8ea-3a8745ddb9d3",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cottonee.Name",
    display_name="Cottonee",
    searchable_by=["Cottonee", "Basic", "Cottonee"],
    subtypes=["Basic"],
    collector_number=147,
    set_code="SM12",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=546,
    abilities=[
        Attack(
            title="Lost March",
            game_text="This attack does 20 damage for each of your Pok\u00e9mon, except p (Prism Star) Pok\u00e9mon, in the Lost Zone.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="x",
            effect=lost_march,
        ),
    ],
)