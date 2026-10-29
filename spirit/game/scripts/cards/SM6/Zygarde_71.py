from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.sm6 import earthen_aura_passive, peace_maker

card = PokemonCardDef(
    guid="b60037e7-5ddf-5ac5-a84d-5584c9e79514",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zygarde.Name",
    display_name="Zygarde",
    searchable_by=["Zygarde", "Basic", "Zygarde"],
    subtypes=["Basic"],
    collector_number=71,
    set_code="SM6",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=718,
    abilities=[
        Ability(
            title="Earthen Aura",
            game_text="Damage from this Pok\u00e9mon's attacks isn't affected by Weakness or Resistance.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=earthen_aura_passive,
        ),
        Attack(
            title="Peace Maker",
            game_text="If your opponent has an Ultra Beast in play, this attack does 30 more damage.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
            damage_operator="+",
            effect=peace_maker,
        ),
    ],
)
