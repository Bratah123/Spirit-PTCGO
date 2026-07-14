from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import heal_attack

card = PokemonCardDef(
    guid="a27fb782-d916-5c91-83a3-08fe541d979e",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Eldegoss.Name",
    display_name="Eldegoss",
    searchable_by=["Eldegoss", "Stage 1", "Eldegoss"],
    subtypes=["Stage 1"],
    collector_number=25,
    set_code="SWSH8",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gossifleur.Name",
    family_id=829,
    abilities=[
        Attack(
            title="Sunny Wind",
            game_text="Heal 20 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=heal_attack(20),
        ),
    ],
)