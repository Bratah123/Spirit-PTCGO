from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import fighting_lightning

card = PokemonCardDef(
    guid="3f367e22-11e1-5729-a443-3c5dd1f83ff1",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zeraora.Name",
    display_name="Zeraora",
    searchable_by=["Zeraora", "Basic", "Zeraora"],
    subtypes=["Basic"],
    collector_number=61,
    set_code="SWSH4",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=807,
    abilities=[
        Attack(
            title="Fighting Lightning",
            game_text="If your opponent's Active Pok\u00e9mon is a Pok\u00e9mon V or Pok\u00e9mon-GX, this attack does 80 more damage.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=fighting_lightning,
        ),
    ],
)
